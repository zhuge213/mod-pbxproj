from pbxproj import PBXGenericObject


class PBXTargetDependency(PBXGenericObject):
    @classmethod
    def create(cls, proxy_ref):
        return cls().parse({
            '_id': cls._generate_id(),
            'isa': cls.__name__,
            'name': proxy_ref.remoteInfo,
            'targetProxy': proxy_ref.get_id()
        })

    def _get_comment(self):
        return 'PBXTargetDependency'
